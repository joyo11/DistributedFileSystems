# Copyright (c) 2025 Mohammad Shafay Joyo
# Licensed under the MIT License.
import os
import random

# Function to create the block directory
def create_blocks_directory(node_num):
    os.makedirs(f"dfs/node_{node_num}/blocks", exist_ok=True)
    print(f"Created dfs/node_{node_num}/blocks")

# Function to split the file into block and store them in nodes with replication
def split_file_into_blocks(file_path, num_nodes=3, block_size=1024, replication_factor=2):
    # Create directories for node
    for i in range(1, num_nodes + 1):
        create_blocks_directory(i)
        
    # Open the file in binary read mode
    with open(file_path, "rb") as f:
        file_data = f.read()

    # Split the file into blocks
    num_blocks = len(file_data) // block_size + (1 if len(file_data) % block_size != 0 else 0)
    blocks = [file_data[i * block_size:(i + 1) * block_size] for i in range(num_blocks)]

    # Store blocks in nodes with replication
    for i, block in enumerate(blocks):
        # Select random nodes for replication
        nodes_to_store = [i % num_nodes]  # Store the block in the node determined by its index
        while len(nodes_to_store) < replication_factor + 1:  # We want at least replication_factor copies
            node_to_add = random.randint(0, num_nodes - 1)
            if node_to_add not in nodes_to_store:
                nodes_to_store.append(node_to_add)

        # Save the block to the selected nodes
        for node_id in nodes_to_store:
            block_file_name = f"block_{i}.bin"
            node_dir = os.path.join("dfs", f"node_{node_id + 1}", "blocks")
            block_path = os.path.join(node_dir, block_file_name)
            with open(block_path, "wb") as block_file:
                block_file.write(block)
            print(f"Block {i} saved to node_{node_id + 1}")

# Function to simulate a node failure by selecting a random node and skipping it
def simulate_node_failure(num_nodes=3):
    failed_node = random.randint(0, num_nodes - 1)
    print(f"Simulating failure for node_{failed_node + 1}")
    return failed_node

# Function to retrieve blocks and reconstruct the original file, skipping a failed node
def retrieve_and_reconstruct_file(output_file_path, num_nodes=3, block_size=1024):
    all_blocks = []

    # Simulate a node failure
    failed_node = simulate_node_failure(num_nodes)
    # Determine the number of blocks by checking the node directories
    node_dirs = [os.path.join("dfs", f"node_{i}", "blocks") for i in range(1, num_nodes + 1)]

    # Collect all blocks from all nodes, skipping the failed node
    for i, node_dir in enumerate(node_dirs):
        if i == failed_node:
            print(f"Skipping node_{i + 1} due to failure.")
            continue  # Skip the failed node
        
        for block_file in os.listdir(node_dir):
            block_path = os.path.join(node_dir, block_file)
            if os.path.isfile(block_path):
                print(f"Found block: {block_file}")  # Debugging output to check the filenames
                with open(block_path, "rb") as block_file:
                    all_blocks.append((block_file.read(), block_file.name))

    # Sort the blocks by the block filename (e.g., block_1.bin, block_2.bin, etc.)
    # We now extract the block number from the file name, not the full path.
    try:
        all_blocks.sort(key=lambda x: int(x[1].split('/')[-1].split('_')[1].split('.')[0]))  # Extract the block number correctly
    except Exception as e:
        print(f"Error sorting blocks: {e}")
        print("Here are the filenames of blocks:", [block[1] for block in all_blocks])
        raise  # Re-raise the exception for debugging

    # Reconstruct the file by writing the blocks to the output file
    with open(output_file_path, "wb") as output_file:
        for block_data, _ in all_blocks:
            output_file.write(block_data)
    print(f"Reconstructed file saved as {output_file_path}")


# Example: Split a file into blocks and store with replication, then reconstruct the file
file_path = "test_data.txt"  # Ensure this file exists in your project directory
split_file_into_blocks(file_path)
retrieve_and_reconstruct_file("reconstructed_file.txt")
