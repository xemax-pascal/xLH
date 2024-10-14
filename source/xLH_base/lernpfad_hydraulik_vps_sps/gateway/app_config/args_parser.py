import argparse
import logging


class ArgsParser:
    def __init__(self):
        self._args = None
        self.command = 'NONE'
        self.db_recreation = False
        self.db_in_memory = False
        self.force_tsl_state_1 = False

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-cmd', '--command', default='NONE', type=str)
        parser.add_argument('--db_recreation', action='store_true')
        parser.add_argument('--db_in_memory', action='store_true')
        parser.add_argument('--force_tsl_state_1', action='store_true')

        self._args = parser.parse_args()
        if self._args.command == 'NONE':
            logging.error('script argument -cmd --command not exist')
            parser.exit(-1, message='script argument -cmd --command not available')

        self.command = self._args.command
        self.db_recreation = self._args.db_recreation
        self.db_in_memory = self._args.db_in_memory
        self.force_tsl_state_1 = self._args.force_tsl_state_1


if __name__ == '__main__':
    pass