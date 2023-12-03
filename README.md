# Very Large Graph

## Authors
Adrien Giget
Denis Stojiljkovic
Ethan Machavoine
Jonathan Poelger
Tanguy Malandain

# Setup
Pour lancer le projet, nous avons suivi les étapes suivantes :

## 1. Configure Spark Master Node
- **Setup Master Process:**
   - Edit the `spark-env.sh` file in the `conf` directory of your Spark installation.
   - Set `SPARK_MASTER_HOST` to the hostname or IP address of the master node.
   - Start the master node with `./start-master.sh` located in the `sbin` directory.

## 2. Configure Spark Worker Nodes
- **Setup Worker Nodes:**
   - Point each worker node to the master by setting the `SPARK_MASTER` environment variable or using the `--master` argument with `./start-worker.sh`.
   - Start the worker node using `./start-worker.sh spark://MASTER:7077`. Replace `MASTER` with the master node's hostname or IP address.

## 3. Submitting Applications

- **Application Submission:**
   - Use the `spark-submit` command to run your PySpark application.
   - Example:
     ```shell
     spark-submit --master spark://MASTER:7077 path_to_your_script.py
     ```

## 4. Versions

- **Versions:**
   - Spark: 3.5.0
   - Python: 3.10
   - Java: 8


## 5. Run & Results

### Cluster before run, during run and after multiple runs
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/cluster_start.png)\
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/cluster_running.png)\
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/cluster_done.png)
### CPU usage before and during run on one of the workers
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/before_run.png)\
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/multiple_cores.png)\
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/high_cpu.png)

### Result of a run
![alt text](https://github.com/Fiwex/vlg_project/blob/main/images/result.png)
