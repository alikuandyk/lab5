class Hypervisor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.virtual_machines = []

    def create_vm(self, vm):
        self.virtual_machines.append(vm)
        print(f"VM {vm.name} created and added to hypervisor {self.name}.")

    def remove_vm(self, vm):
        if vm in self.virtual_machines:
            self.virtual_machines.remove(vm)
            print(f"VM {vm.name} removed from hypervisor {self.name}.")
        else:
            print(f"Error: VM {vm.name} not found in hypervisor {self.name}.")

    def list_vms(self):
        print(f"Hypervisor {self.name} manages the following VMs:")
        for vm in self.virtual_machines:
            print(f"VM ID: {vm.id}, Name: {vm.name}")