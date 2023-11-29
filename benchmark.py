from pyspark import SparkContext
import random


def calculate_sqrt(number):
    return number ** 0.5


if __name__ == "__main__":
    # Initialize SparkContext
    sc = SparkContext(appName="PySparkBenchmark")

    # Number of samples to be generated for each partition
    num_samples_per_partition = 50_000_000

    # Creating an RDD of random numbers
    rdd = sc.parallelize([random.random() for _ in range(num_samples_per_partition)], numSlices=50)

    # Map operation to calculate square root of each number
    sqrt_rdd = rdd.map(calculate_sqrt)

    # Action to trigger the computation
    sqrt_rdd.count()

    sc.stop()
