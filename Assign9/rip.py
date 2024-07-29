import time
import tkinter as tk

class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.routing_table = {}

    def update_routing_table(self, source_router_id, routes):
        for dest, cost in routes.items():
            if dest not in self.routing_table or self.routing_table[dest][0] > cost + self.routing_table[source_router_id][0]:
                self.routing_table[dest] = (cost + self.routing_table[source_router_id][0], source_router_id)

    def get_routing_table(self):
        return self.routing_table

class RIPSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("RIP Simulator")

        self.routers = {
            1: Router(1),
            2: Router(2),
            3: Router(3)
        }

        # Initialize initial routing tables
        self.routers[1].routing_table = {2: (1, 2), 3: (3, 3)}
        self.routers[2].routing_table = {1: (1, 1), 3: (2, 3)}
        self.routers[3].routing_table = {1: (3, 1), 2: (2, 2)}

        self.create_gui()
        self.simulate_rip()  # Call the simulation function initially

    def create_gui(self):
        self.label = tk.Label(self.root, text="Routing Tables:")
        self.label.pack()

        self.text = tk.Text(self.root, width=30, height=15)
        self.text.pack()

        self.update_button = tk.Button(self.root, text="Update", command=self.simulate_rip)
        self.update_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

    def update_routing_tables_text(self, text):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text)

    def simulate_rip(self):
        router1 = self.routers[1]
        router2 = self.routers[2]
        router3 = self.routers[3]

        router2.update_routing_table(1, {3: 2})

        routing_tables = ""
        for router_id, router in self.routers.items():
            routing_tables += f"Router {router_id}:\n"
            for dest, (cost, next_hop) in router.get_routing_table().items():
                routing_tables += f"Destination: {dest}, Cost: {cost}, Next Hop: Router {next_hop}\n"
            routing_tables += "\n"

        self.update_routing_tables_text(routing_tables)

if __name__ == '__main__':
    root = tk.Tk()
    app = RIPSimulator(root)
    root.mainloop()
