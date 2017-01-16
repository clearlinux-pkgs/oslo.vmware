#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : oslo.vmware
Version  : 2.15.0
Release  : 41
URL      : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.15.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.15.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.15.0.tar.gz.asc
Summary  : Oslo VMware library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.vmware-python
BuildRequires : GitPython-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : bandit-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : imagesize-python
BuildRequires : mox3-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.concurrency-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : suds-jurko-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : urllib3-python
BuildRequires : virtualenv

%description
===================================================
oslo.vmware --- VMware support code for OpenStack
===================================================

%package python
Summary: python components for the oslo.vmware package.
Group: Default
Requires: PyYAML-python
Requires: eventlet-python
Requires: netaddr
Requires: oslo.concurrency-python
Requires: requests-python
Requires: suds-jurko-python
Requires: urllib3-python

%description python
python components for the oslo.vmware package.


%prep
%setup -q -n oslo.vmware-2.15.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484559311
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484559311
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
