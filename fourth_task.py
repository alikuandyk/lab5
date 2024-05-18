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
            print(f"Running {app} on {self.name}")
        else:
            print(f"Error: Not enough resources to run {app} on {self.name}.")

    def stop_app(self, app, cpu, memory, storage):
        for running_app in self.running_apps:
            if running_app['app'] == app and running_app['cpu'] == cpu and running_app['memory'] == memory and running_app['storage'] == storage:
                self.running_apps.remove(running_app)
                self.available_cpu += cpu
                self.available_memory += memory
                self.available_storage += storage
                print(f"Stopped {app} on {self.name}. Freed up CPU: {cpu}, Memory: {memory}, Storage: {storage}")
                return
        print(f"Error: App {app} is not running on {self.name}.")

    def show_specs(self):
        print(f"VM Name: {self.name}, CPU: {self.available_cpu}/{self.total_cpu}, Memory: {self.available_memory}/{self.total_memory}, Storage: {self.available_storage}/{self.total_storage}")

    def calculate_utilization(self, cpu_used, memory_used, storage_used):
        cpu_utilization = (cpu_used / self.total_cpu) * 100
        memory_utilization = (memory_used / self.total_memory) * 100
        storage_utilization = (storage_used / self.total_storage) * 100
        return cpu_utilization, memory_utilization, storage_utilization

class Hypervisor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.virtual_machines = []

    def create_vm(self, vm):
        self.virtual_machines.append(vm)
        print(f"Created VM {vm.name} on {self.name}")

    def remove_vm(self, vm):
        if vm in self.virtual_machines:
            self.virtual_machines.remove(vm)
            print(f"Removed VM {vm.name} from {self.name}")
        else:
            print(f"Error: VM {vm.name} not found in {self.name}.")

    def list_vms(self):
        print(f"Hypervisor {self.name} manages the following VMs:")
        for vm in self.virtual_machines:
            print(f"VM ID: {vm.id}, VM Name: {vm.name}")

# Scenario execution
hypervisor = Hypervisor(1, "Hypervisor1")

# Create Virtual Machines
vm1 = VirtualMachine(1, "VM1", 2, 8, 500)
vm2 = VirtualMachine(2, "VM2", 4, 16, 1000)

# Add the virtual machines to the hypervisor
hypervisor.create_vm(vm1)
hypervisor.create_vm(vm2)

# List all virtual machines on the hypervisor
hypervisor.list_vms()

# Show the specifications of each virtual machine
vm1.show_specs()
vm2.show_specs()

# Run applications on each virtual machine
vm1.run_app("App1", 1, 2, 125)
vm1.run_app("App2", 1, 2, 125)

vm2.run_app("App1", 1, 12, 750)
vm2.run_app("App2", 1, 4, 250)

# Stop the applications on each virtual machine
vm1.stop_app("App1", 1, 2, 125)
vm1.stop_app("App2", 1, 2, 125)

vm2.stop_app("App1", 1, 12, 750)
vm2.stop_app("App2", 1, 4, 250)

# Show the specifications of each virtual machine after stopping the applications
vm1.show_specs()
vm2.show_specs()

# Calculate and print the resource utilization
cpu_used_vm1 = 1 + 1  # CPUs used by App1 and App2
memory_used_vm1 = 2 + 2  # Memory used by App1 and App2
storage_used_vm1 = 125 + 125  # Storage used by App1 and App2

cpu_used_vm2 = 1 + 1  # CPUs used by App1 and App2
memory_used_vm2 = 12 + 4  # Memory used by App1 and App2
storage_used_vm2 = 750 + 250  # Storage used by App1 and App2

cpu_utilization_vm1, memory_utilization_vm1, storage_utilization_vm1 = vm1.calculate_utilization(cpu_used_vm1, memory_used_vm1, storage_used_vm1)
cpu_utilization_vm2, memory_utilization_vm2, storage_utilization_vm2 = vm2.calculate_utilization(cpu_used_vm2, memory_used_vm2, storage_used_vm2)

print(f"Resource utilization for VM1 - CPU: {cpu_utilization_vm1}%, Memory: {memory_utilization_vm1}%, Storage: {storage_utilization_vm1}%")
print(f"Resource utilization for VM2 - CPU: {cpu_utilization_vm2}%, Memory: {memory_utilization_vm2}%, Storage: {storage_utilization_vm2}%")
