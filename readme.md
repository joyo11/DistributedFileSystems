# Distributed File System with Node Failure Simulation

## Project Overview
This project implements a **Distributed File System (DFS)** that simulates a file storage and retrieval system across multiple nodes. It ensures data availability by simulating node failures and reconstructing files using replication.

## Problem Statement
The primary goal was to build a simple DFS where files are split into blocks, stored across multiple nodes, and reconstructed upon request. The system simulates node failures and continues to provide data availability by skipping failed nodes and using available replicas of the blocks.

## Key Features
- **Block-level File Storage**: Files are split into blocks and stored on multiple nodes with replication for data redundancy.
- **Node Failure Simulation**: Simulates a node failure and skips it during file reconstruction to ensure data availability.
- **File Reconstruction**: The system retrieves blocks from active nodes and reconstructs the original file.
- **Python & Flask**: Utilizes Flask for managing the storage, retrieval, and file reconstruction operations.

## Technology Stack
- **Backend**: Python, Flask
- **File Handling**: Local file system for storing and managing blocks
- **File Splitter**: Blocks of a file are distributed across multiple nodes
- **Failure Simulation**: Randomly selects a node to simulate failure and skip it during reconstruction

## How It Works
1. **File Splitting**: The file is divided into fixed-size blocks, each block stored on multiple nodes.
2. **Node Failure Simulation**: A random node is simulated to fail during file retrieval.
3. **File Reconstruction**: The system gathers all the available blocks from the remaining nodes and reconstructs the original file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/joyo11/DistributedFileSystems.git
