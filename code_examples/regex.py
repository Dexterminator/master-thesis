class RegexpExtractFilter(Filter):
    def prepare(self, config, pipeline):
        self.regex = config.regex
        self.field = config.field
        self.destination = config.destination 
        self.destination_field = config.destination_field

    def process_record(self, record, pipeline):
        value = record.fields[self.field]
        match = self.regex.search(value)
        if match:
            if self.destination == 'record':
                record.fields[self.destination_field] = match
            elif self.destination == 'variable':
                pipeline.globals[self.destination_field] = match
