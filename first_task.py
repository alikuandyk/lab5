class VirtualMachine:
    def __init__(self, id, name, cpu, memory, storage):
        self.id = id
        self.name = name
        self.total_cpu = cpu
        self.total_memory = memory
        self.total_storage = storage
        self.available_cpu = cpu
        self.available_memory = memory
        self.available_storage = storage
        self.running_apps = []

    def run_app(self, app, cpu, memory, storage):
        if cpu <= self.available_cpu and memory <= self.available_memory and storage <= self.available_storage:
            self.running_apps.append({'app': app, 'cpu': cpu, 'memory': memory, 'storage': storage})
            self.available_cpu -= cpu
            self.available_memory -= memory
            self.available_storage -= storage
            print(f"App {app} is running.")
        else:
            print(f"Error: Not enough resources to run {app}.")

    def stop_app(self, app, cpu, memory, storage):
        for running_app in self.running_apps:
            if running_app['app'] == app and running_app['cpu'] == cpu and running_app['memory'] == memory and running_app['storage'] == storage:
                self.running_apps.remove(running_app)
                self.available_cpu += cpu
                self.available_memory += memory
                self.available_storage += storage
                print(f"App {app} has been stopped.")
                return
        print(f"Error: App {app} is not running.")

    def show_specs(self):
        print(f"VM ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Total CPU: {self.total_cpu}")
        print(f"Total Memory: {self.total_memory}")
        print(f"Total Storage: {self.total_storage}")
        print(f"Available CPU: {self.available_cpu}")
        print(f"Available Memory: {self.available_memory}")
        print(f"Available Storage: {self.available_storage}")
        print(f"Running Applications: {self.running_apps}")
