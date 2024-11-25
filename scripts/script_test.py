import pandas as pd
from tempfile import NamedTemporaryFile


def main() :
    with NamedTemporaryFile("w", suffix='.csv') as f:

        df = pd.DataFrame()
        df.to_csv(f.name, sep=';', decimal=',', index=False)
        print(f.name)





if __name__ == '__main__':
    raise SystemExit(main())