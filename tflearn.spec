#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tflearn
Version  : 0.3.2
Release  : 24
URL      : https://github.com/tflearn/tflearn/archive/0.3.2.tar.gz
Source0  : https://github.com/tflearn/tflearn/archive/0.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: tflearn-python3
Requires: tflearn-license
Requires: tflearn-python
Requires: Pillow
Requires: numpy
Requires: six
BuildRequires : Pillow
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
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
Requires: tflearn-python3

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531171880
find -name "*pyx" | xargs touch ||:
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/tflearn
cp LICENSE %{buildroot}/usr/share/doc/tflearn/LICENSE
cp docs/templates/license.md %{buildroot}/usr/share/doc/tflearn/docs_templates_license.md
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/tflearn/LICENSE
/usr/share/doc/tflearn/docs_templates_license.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/tests/__init__.py
%exclude /usr/lib/python3.7/site-packages/tests/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3*/*
