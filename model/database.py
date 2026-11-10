import sys
from pathlib import Path
from typing import Any, Generator
import conf
from uuid import uuid4, UUID
import csv

EXEMPLE_FILENAME = "exemple.csv"

class Table:
    path: Path
    fields: set[str, ...]
    rows: dict[UUID, dict[str, str]]

    def __init__(self, datadir: Path, filename: str, fields: set[str]):
        self.path = datadir / filename
        if "uuid" in fields:
            raise ValueError("Table fields must not contain \"uuid\". It is automatically added")
        self.fields = {"uuid"} | fields
        self.rows = dict()
    
    def insert_row(self, values: dict[str, str]) -> str:
        # errors
        user_fields = self.fields.difference({"uuid"});
        invalid = set(values.keys()).difference(user_fields)
        if len(invalid) > 0:
            raise ValueError(f"Invalid fields provided: {invalid}")
        missing = user_fields.difference(values.keys())
        if len(missing) > 0:
            raise ValueError(f"Missing fields: {missing}")
        # save new record
        uuid = uuid4()
        self.rows[uuid] = values | { "uuid": str(uuid) }
        self.write_to_file()
        return str(uuid)
    
    def get_row_by_uuid(self, uuid: str) -> dict[str, str]:
        return self.rows[UUID(uuid)]
    
    def get_all_rows(self) -> list[dict[str, str]]:
        self.read_from_file()
        return self.rows.values()
    
    def __iter__(self) -> Generator[dict[str, str], Any, Any]:
        for row in self.get_all_rows():
            yield row
    
    def __len__(self) -> int:
        return len(self.rows)
    
    def get_rows_by(self, field: str, value: str) -> list[dict[str, str]]:
        return [row for row in self.get_all_rows() if row[field] == value]
    
    def get_row_by(self, field: str, value: str) -> dict[str, str]:
        matches = self.get_rows_by(field)
        if len(matches) > 0:
            first_match = matches[0]
            return first_match
        else:
            return None

    def write_to_file(self):
        with open(self.path, "w", newline="") as file:
            print("Writing database table ", self.path)
            writer = csv.DictWriter(file, db.exemple.fields)
            writer.writeheader()
            writer.writerows(self.rows.values())
    
    def read_from_file(self):
        with open(db.exemple.path, "r") as file:
            print("Reading database table ", self.path)
            data = csv.DictReader(file)
            self.rows.clear()
            for row in data:
                uuid = UUID(row["uuid"])
                self.rows[uuid] = { key:value for key, value in row.items() }

    def keys(self) -> tuple[UUID]:
        return self.rows.keys()

    def __getitem__(self, key: UUID) -> dict[str, str]:
        return self.rows[key]

class Db:
    exemple: Table

    def __init__(self):
        # get data dir
        datadir = Db._create_and_get_datadir()
        # create tables
        self.exemple = Table(datadir, EXEMPLE_FILENAME, {"name", "age"})

    @staticmethod
    def _get_datadir() -> Path:
        """
        Code de Stack Overflow

        Returns a parent directory path
        where persistent application data can be stored.

        # linux: ~/.local/share
        # macOS: ~/Library/Application Support
        # windows: C:/Users/<USER>/AppData/Roaming
        """

        home = Path.home()
        if sys.platform == "win32":
            return home / "AppData/Roaming"
        elif sys.platform == "linux":
            return home / ".local/share"
        elif sys.platform == "darwin":
            return home / "Library/Application Support"

    @staticmethod
    def _create_and_get_datadir() -> Path:
        my_datadir = Db._get_datadir() / conf.APP_NAME
        my_datadir.mkdir(parents=True, exist_ok=True)
        return my_datadir

if __name__ == "__main__":
    # tests
    db = Db()
    # exemple headers
    # print(db.exemple.get_headers())
    db.exemple.insert_row({ "name": "luis", "age": str(10) })
    db.exemple.insert_row({ "name": "pepito", "age": str(12) })
    db.exemple.insert_row({ "name": "maria", "age": str(30) })
    db.exemple.insert_row({ "name": "artura", "age": str(28) })
    print("created table exemple:")
    print(dict(db.exemple))
    db.exemple.write_to_file()
    db.exemple.read_from_file()
    print("read table exemple:")
    print(dict(db.exemple))
        

    