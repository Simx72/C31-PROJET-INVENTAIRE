import sys
from pathlib import Path
from typing import Any, Generator
import conf
from uuid import uuid4, UUID
import csv

EXEMPLE_FILENAME = "exemple.csv"

class Row:
    _headers: tuple[str, ...]
    _values: tuple[str, ...]
    def __init__(self, headers: tuple[str, ...], id: UUID, values: tuple[str, ...]) -> None:
        self._headers = ("uuid",) + headers
        self._values = (str(id),) + values
    
    def get_str(self, key: str) -> str:
        try:
            index = self._headers.index(key)
            return self._values[index]
        except ValueError:
            raise ValueError(f"No key {key} in this table. Did you mispelled the column name ?")

    def get_int(self, key: str) -> int:
        return int(self.get_str(key))

    def get_float(self, key: str) -> float:
        return float(self.get_str(key))

    def to_dict(self) -> dict[str, str]:
        my_dict: dict[str, str] = {}
        for header, value in list(zip(self._headers, self._values)):
            my_dict[header] = value
        return my_dict

class NotFoundException(Exception):
    pass

class Table:
    path: Path
    data: None
    _headers: tuple[str, ...]
    _rows: dict[UUID, tuple[str, ...]]

    def __init__(self, datadir: Path, filename: str, headers: tuple[str, ...]):
        self.path = datadir / filename
        if "uuid" in headers:
            raise ValueError("Headers must not contain \"uuid\" in its values")
        self._headers = headers
        self._rows = {}
    
    def get_headers(self) -> list[str]:
        return ["uuid"] + list(self._headers)
    
    def insert_row(self, values: tuple[str, ...]) -> UUID:
        if len(values) != len(self._headers):
            raise ValueError("Invalid number of values: ", values)
        uuid = uuid4()
        self._rows[uuid] = values
        return uuid
    
    def get_row_by_uuid(self, uuid: UUID) -> Row:
        return Row(self._headers, uuid, self._rows[uuid])
    
    def get_all_rows(self) -> list[Row]:
        return [Row(self._headers, uuid, values) for uuid, values in self._rows.items()]
    
    def __iter__(self) -> Generator[Row, Any, Any]:
        for row in self.get_all_rows():
            yield row
    
    def __len__(self) -> int:
        return len(self._rows)
    
    def get_row_by(self, field: str, value: str) -> Row:
        try:
            fieldindex = self._headers.index(field)
            matches = [Row(self._headers, uuid, values) for uuid, values in self._rows.items() if values[fieldindex] == value]
            if len(matches) > 0:
                first_match = matches[0]
                return first_match
            else:
                raise NotFoundException
        except ValueError:
            raise ValueError(f"Field {field} not present in table. Did you mispelled field name? Available fields: {self.get_headers()}")
    
    def write_to_file(self):
        with open(self.path, "w", newline="") as file:
            print("Writing database table ", self.path)
            # print("Writing with headers: ", db.exemple.get_headers())
            writer = csv.DictWriter(file, db.exemple.get_headers())
            writer.writeheader()
            for row in db.exemple:
                # print("Writing ", row.to_dict())
                writer.writerow(row.to_dict())
    
    def read_to_file(self):
        with open(db.exemple.path, "r") as file:
            print("Reading database table ", self.path)
            data = csv.DictReader(file)
            for row in data:
                self._rows.clear()
                self.insert_row() # fix later...
                # print("Reading ", row)

class Db:
    exemple: Table

    def __init__(self):
        # get data dir
        datadir = Db._create_and_get_datadir()
        # create tables
        self.exemple = Table(datadir, EXEMPLE_FILENAME, ("name", "age"))

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
    db.exemple.insert_row(("luis", str(10)))
    db.exemple.insert_row(("pepito", str(12)))
    db.exemple.insert_row(("maria", str(30)))
    db.exemple.insert_row(("artura", str(28)))
    db.exemple.write_to_file()
    db.exemple.read_to_file()

    