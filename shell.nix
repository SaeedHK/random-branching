{ pkgs ? import (builtins.fetchTarball {
  name = "nixos-unstable-2020-09-14";
  url = "https://github.com/nixos/nixpkgs/archive/684d691c6e9d49d3aab96f4053d011c225aa75bf.tar.gz";
  sha256 = "005dcykphjfl8kzall2njarl1prb16mbix072gk6sq2wgfp1ba02";
}) {}}:
with pkgs;
let
  my-python-packages = python-packages: with python-packages; [
    numpy
    matplotlib
  ]; 
  python-with-my-packages = python3.withPackages my-python-packages;
in
mkShell {
  buildInputs = [
    python-with-my-packages
  ];
}
