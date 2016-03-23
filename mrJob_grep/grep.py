"""Return all input lines matching the given expression."""
from mrjob.job import MRJob
from mrjob.util import cmd_line


class MRGrepJob(MRJob):

    def configure_options(self):
        super(MRGrepJob, self).configure_options()

        self.add_passthrough_option(
            '-e', '--expression', type='str', default=None,
            help=( 'Expression to search for. Required.'))

    def mapper_cmd(self):
        if self.options.expression is None:
            raise ValueError("Must specify --expression")
        return cmd_line(['grep', '-e', self.options.expression])


if __name__ == '__main__':
    MRGrepJob().run()
