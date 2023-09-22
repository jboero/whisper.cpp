# SRPM for building from source and packaging an RPM for RPM-based distros.
# https://fedoraproject.org/wiki/How_to_create_an_RPM_package
# Built and maintained by John Boero - boeroboy@gmail.com
# In honor of Seth Vidal https://www.redhat.com/it/blog/thank-you-seth-vidal

# Notes for whisper.cpp:
# 1. There are currently no tags - which will not sort asciibetically.
#    We need to declare standard versioning if people want to sort latest releases.
#    In the meantime, YYYYMMDD build date will be used for packaging.
# 2. Builds for CUDA/OpenCL support are separate, with different depenedencies.
# 3. NVidia's developer repo must be enabled with nvcc, cublas, clblas, etc installed.
#    Example: https://developer.download.nvidia.com/compute/cuda/repos/fedora37/x86_64/cuda-fedora37.repo
# 4. OpenCL/CLBLAST support simply requires the ICD loader and basic opencl libraries.
#    It is up to the user to install the correct vendor-specific support.

Name:           libwhisper
Version:        %( date "+%%Y%%m%%d" )
Release:        1%{?dist}
Summary:        Library CPU Inference of Whisper in C/C++ with OpenCL CLBLAS option.
License:        MIT
Source0:        https://github.com/ggerganov/whisper.cpp/archive/refs/heads/master.tar.gz
BuildRequires:  coreutils make gcc-c++ git libstdc++-devel
Requires:       libstdc++
URL:            https://github.com/ggerganov/whisper.cpp

%define debug_package %{nil}
%define source_date_epoch_from_changelog 0

%description
Inference library with optional OpenCL support for Meta's Whisper models using default options.
Models are not included in this package and must be downloaded separately.

%prep
%setup -n whisper.cpp-master

%build
make -j libwhisper.so

%install
mkdir -p %{buildroot}%{_libdir}/
cp -p libwhisper.so %{buildroot}%{_libdir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/*

%files
%{_libdir}/libwhisper.so

%pre
%post
%preun
%postun
%changelog
