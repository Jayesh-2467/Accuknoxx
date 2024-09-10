import time
import threading
from django.db import transaction
from django.dispatch import receiver, Signal

# Custom signal
my_signal = Signal()

# Signal handler for Question 1 (Synchronous Execution)
@receiver(my_signal)
def synchronous_handler(sender, **kwargs):
    print("Synchronous Signal handler started")
    time.sleep(2)  # Simulate a long-running task
    print("Synchronous Signal handler finished")

# Signal handler for Question 2 (Same Thread Execution)
@receiver(my_signal)
def thread_check_handler(sender, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

# Signal handler for Question 3 (Same Transaction Execution)
@receiver(my_signal)
def transaction_handler(sender, **kwargs):
    print("Signal handler inside transaction")

# Function to test transaction
@transaction.atomic
def transactional_operation():
    print("Transaction started")
    my_signal.send(sender=None)  # Emit signal inside a transaction
    print("Transaction finished")
