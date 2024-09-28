def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem.

    :param n: Number of disks
    :param source: The source peg
    :param auxiliary: The auxiliary peg
    :param target: The target peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n-1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, source, target)

# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'B', 'C')
