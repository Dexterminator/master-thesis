class GlobalVariableFilter(Filter):
    def prepare(self, config, pipeline):
        self.variable_name = config.variable_name
        pipeline.globals.init(self.variable_name)
