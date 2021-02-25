from Repository.Repo import RepoOrder
from Controller.controller import Controller
from Domain.order import Order
from UI.UI import UI
from collections import deque

order1 = Order(1, ["adidasi", "papuci", "tricouri"], "cash", 576)
order2 = Order(2, ["proteine", "papuci", "caciule"], "cash", 890)
order3 = Order(3, ["adidasi", "sandale", "energizante"], "cash", 1120)

repo = RepoOrder([order1, order2, order3])

controller = Controller(repo)

operation_stack = deque()

UI = UI(controller)
UI.main_menu()