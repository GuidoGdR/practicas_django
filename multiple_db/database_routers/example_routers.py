#Routers of DB


class ExampleRouter:
    
    router_app_labels={'apps.example'}

    def db_for_read(self, model, **kwargs):
        if model._meta.app_label in self.router_app_labels:
            return 'example_db'
        return None
    
    def db_for_write(self, model, **kwargs):
        if model._meta.app_label in self.router_app_labels:
            return 'example_db'
        return None
    
    def allow_relation(self, obj1, obj2, **kwargs):
        if (
            obj1._meta.app_label in self.router_app_labels
            or
            obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **kwargs):
        if app_label in self.router_app_labels:
            return db == 'example_db'
        return None
    