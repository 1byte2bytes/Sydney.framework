# SydChain

This is a toolchain I'm developing myself. The macOS one tends to be a bit wonky for some projects, so I'm just gonna make my own!

```
cd SydChain
source scripts/vars
./scripts/bootstrap.sh
python3 scripts/build.py
```

## Supported langauges so far:

```
x86(_64) Assembly, C, C++, Objective-C, Objective-C++, C#, D, Rust

OpenMP, OpenCL, CUDA
```

## Possible upcoming languages:

**This list is not a guarantee, it's mostly just stuff I see configure commonly ask for and can be slotted into LLVM.**

```
FORTRAN (Flang?), Java, Swift
```
