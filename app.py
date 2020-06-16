import sys
import config


def main():
    """Program expects 1 argument when executed."""

    ## TODO: Write wrapper function to test argument passed before invoking main()
    env = sys.argv[1]
    db_details = config.DB_DETAILS.get(env)
    source_db_details = db_details.get('SOURCE_DB')
    print(source_db_details.get('DB_USER'))
    print(source_db_details.get('DB_PASS'))


if __name__ == '__main__':
    main()