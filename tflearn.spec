#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tflearn
Version  : 0.3.2
Release  : 31
URL      : https://github.com/tflearn/tflearn/archive/0.3.2.tar.gz
Source0  : https://github.com/tflearn/tflearn/archive/0.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: tflearn-license = %{version}-%{release}
Requires: tflearn-python = %{version}-%{release}
Requires: tflearn-python3 = %{version}-%{release}
Requires: Pillow
Requires: numpy
Requires: six
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : six

%description
[![Build Status](https://travis-ci.org/tflearn/tflearn.svg?branch=master)](https://travis-ci.org/tflearn/tflearn)
[![PyPI version](https://badge.fury.io/py/tflearn.svg)](https://badge.fury.io/py/tflearn)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Join the chat at https://gitter.im/einsteinsci/betterbeginnings](https://badges.gitter.im/tflearn/tflearn.svg)](https://gitter.im/tflearn/tflearn?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package license
Summary: license components for the tflearn package.
Group: Default

%description license
license components for the tflearn package.


%package python
Summary: python components for the tflearn package.
Group: Default
Requires: tflearn-python3 = %{version}-%{release}

%description python
python components for the tflearn package.


%package python3
Summary: python3 components for the tflearn package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tflearn package.


%prep
%setup -q -n tflearn-0.3.2
cd %{_builddir}/tflearn-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576091623
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tflearn
cp %{_builddir}/tflearn-0.3.2/LICENSE %{buildroot}/usr/share/package-licenses/tflearn/160a567114059e206b2b69877dac19c93a467b75
cp %{_builddir}/tflearn-0.3.2/docs/templates/license.md %{buildroot}/usr/share/package-licenses/tflearn/160a567114059e206b2b69877dac19c93a467b75
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")
rm -rfv %{buildroot}/${sitedir}/tests
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tflearn/160a567114059e206b2b69877dac19c93a467b75

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
