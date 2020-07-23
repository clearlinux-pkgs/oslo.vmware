#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.vmware
Version  : 3.6.0
Release  : 70
URL      : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-3.6.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-3.6.0.tar.gz
Source1  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-3.6.0.tar.gz.asc
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
Requires: stevedore
Requires: suds-jurko
Requires: urllib3
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : lxml
BuildRequires : netaddr
BuildRequires : oslo.concurrency
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : stevedore
BuildRequires : suds-jurko
BuildRequires : urllib3

%description
Team and repository tags
        ========================

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
Provides: pypi(oslo.vmware)
Requires: pypi(eventlet)
Requires: pypi(lxml)
Requires: pypi(netaddr)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.context)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(stevedore)
Requires: pypi(suds_jurko)
Requires: pypi(urllib3)

%description python3
python3 components for the oslo.vmware package.


%prep
%setup -q -n oslo.vmware-3.6.0
cd %{_builddir}/oslo.vmware-3.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595516375
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.vmware
cp %{_builddir}/oslo.vmware-3.6.0/LICENSE %{buildroot}/usr/share/package-licenses/oslo.vmware/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.vmware/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
