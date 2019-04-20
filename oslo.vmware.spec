#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.vmware
Version  : 2.32.2
Release  : 52
URL      : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.32.2.tar.gz
Source0  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.32.2.tar.gz
Source99 : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.32.2.tar.gz.asc
Summary  : Oslo VMware library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.vmware-license = %{version}-%{release}
Requires: oslo.vmware-python = %{version}-%{release}
Requires: oslo.vmware-python3 = %{version}-%{release}
Requires: PyYAML
Requires: eventlet
Requires: lxml
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
Requires: suds-jurko
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.vmware.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the oslo.vmware package.
Group: Default

%description license
license components for the oslo.vmware package.


%package python
Summary: python components for the oslo.vmware package.
Group: Default
Requires: oslo.vmware-python3 = %{version}-%{release}

%description python
python components for the oslo.vmware package.


%package python3
Summary: python3 components for the oslo.vmware package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.vmware package.


%prep
%setup -q -n oslo.vmware-2.32.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551396383
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.vmware
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.vmware/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.vmware/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
