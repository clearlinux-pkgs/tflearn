#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tflearn
Version  : a9f86d8df475706f76e5c0e98210b7d4faf02206
Release  : 3
URL      : https://github.com/tflearn/tflearn/archive/a9f86d8df475706f76e5c0e98210b7d4faf02206.tar.gz
Source0  : https://github.com/tflearn/tflearn/archive/a9f86d8df475706f76e5c0e98210b7d4faf02206.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: tflearn-python
BuildRequires : Pillow
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
[![Build Status](https://travis-ci.org/tflearn/tflearn.svg?branch=master)](https://travis-ci.org/tflearn/tflearn)
[![PyPI version](https://badge.fury.io/py/tflearn.svg)](https://badge.fury.io/py/tflearn)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Join the chat at https://gitter.im/einsteinsci/betterbeginnings](https://badges.gitter.im/tflearn/tflearn.svg)](https://gitter.im/tflearn/tflearn?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package python
Summary: python components for the tflearn package.
Group: Default

%description python
python components for the tflearn package.


%prep
%setup -q -n tflearn-a9f86d8df475706f76e5c0e98210b7d4faf02206

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486268281
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
