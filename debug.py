from benchmark import PyTorchBenchmark, PyTorchBenchmarkArguments

args = PyTorchBenchmarkArguments(models=['gpt2'])
benchmark = PyTorchBenchmark(args)
results = benchmark.run()