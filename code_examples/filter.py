class Filter(object):
    def prepare(self, config, pipeline):
        pass

    def pre_process_record(self, record, pipeline):
        pass

    def process_record(self, record, pipeline):
        pass

    def post_process_record(self, record, pipeline):
        pass
