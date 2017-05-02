#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : oslo.vmware
Version  : 2.19.0
Release  : 46
URL      : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.19.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.19.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.19.0.tar.gz.asc
Summary  : Oslo VMware library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.vmware-python
Requires: PyYAML
Requires: eventlet
Requires: lxml
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
Requires: suds-jurko
Requires: urllib3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/badges/oslo.vmware.svg
:target: https://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the oslo.vmware package.
Group: Default

%description python
python components for the oslo.vmware package.


%prep
%setup -q -n oslo.vmware-2.19.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491343003
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1491343003
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
