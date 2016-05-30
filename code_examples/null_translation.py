class NullTranslationFilter(Filter):
    def prepare(self, config, pipeline):
        self.null_tokens = config.null_tokens

    def process_record(self, record, pipeline):
        for field, value in record.fields.items():
            if value in self.null_tokens:
                record.fields[field] = None
