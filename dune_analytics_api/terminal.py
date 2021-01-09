import readline

from prettytable import PrettyTable

from .query_maker import QueryError


class Terminal:
    def __init__(self, query_maker):
        self._query_maker = query_maker
        self._download = None

    def run(self):
        query = ""
        while True:
            prompt = "  " if query else "> "

            query_part = input(prompt)
            query += " " + query_part
            query = query.strip()

            if not query:
                continue

            if query == 'exit':
                break

            if query.startswith("download"):
                self._download = query.split(None, 1)[1]
                query = ""
                continue

            if query.endswith(";"):
                try:
                    table = self._perform_query(query)
                except QueryError as exc:
                    print(f"Error: {exc.args[0]}")
                else:
                    if self._download is None:
                        print(table)
                    else:
                        with open(self._download, 'w') as f:
                            f.write(table.get_csv_string())
                        print(f"Saved to {self._download}")
                    self._download = None
                query = ""

    def _perform_query(self, query):
        rows = self._query_maker.exec(query)
        if rows:
            table = PrettyTable(rows[0].keys())
            for row in rows:
                table.add_row(row.values())
            return table

        else:
            return None
