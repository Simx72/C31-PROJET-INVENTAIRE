import sys
from pathlib import Path
import conf
from uuid import uuid4, UUID

EXEMPLE_FILENAME = "exemple.csv"

class Row:
    _headers: tuple[str, ...]
    _values: tuple[str, ...]
    def __init__(self, _headers: tuple[str, ...], id: UUID, values: tuple[str, ...]) -> None:
        self._headers = _headers
        tmp_values: list[str] = []
        tmp_values.append(str(id))
        self.values = values
    
    def get_str(self, key: str) -> str:
        try:
            index = self._headers.index(key)
            return self.values[index]
        except ValueError:
            raise ValueError(f"No key {key} in this table. Did you mispelled the column name ?")

    def get_int(self, key: str) -> int:
        return int(self.get_str(key))

    def get_float(self, key: str) -> float:
        return float(self.get_str(key))

class TableData:
    _headers: tuple[str, ...]
    _rows: dict[UUID, tuple[str, ...]]

    def __init__(self, headers: tuple[str, ...]):
        # Dans le headers, on ne peut pas avoir l'ID,
        # Il est rajouté obligatoirement à chaque table
        if "id" in headers:
            raise ValueError("Headers must not contain \"id\" in its values")
        self._headers = headers
        self._rows = {}
    
    def insert_row(self, values: tuple[str]) -> UUID:
        if len(values) != len(self._headers):
            raise ValueError("Invalid number of values: ", values)
        id = uuid4()
        self._rows[id] = values
        return id
    
    def get_row(self, id: UUID) -> Row:
        return Row(self._headers, id, self._rows[id])
    
    def get_all_rows(self) -> list[Row]:
        rows: list[Row] = []
        for id, values in self._rows.items():
            row = Row(self._headers, id, values)
            rows.append(row)
        return rows

class Table:
    path: Path
    data: TableData

    def __init__(self, datadir: Path, filename: str, headers: tuple[str, ...]):
        self.path = datadir / filename
        self.data = TableData(headers)

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
    print(db.exemple.path)
    print(db.exemple.data.get_all_rows())

    