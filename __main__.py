import sys
from nbibliothek.service import NbibliothekService


def get_db(sys_arg):
    for arg in sys_arg:
        url = arg.split("-db:url=")
        try:
            return url[1]
        except:
            pass
    return 'library.db'

if __name__ == '__main__':
    db_url = r'J:/nbibliothek/nbibliothek/library.db'
    apps = NbibliothekService(db_url)

    arg = sys.argv[1]
    url = get_db(arg)

    init_table = "-db:init=True"
    if arg.lower().split("-db:init=") == init_table.lower().split("-db:init="):
        apps.init_db()

    apps.run()

