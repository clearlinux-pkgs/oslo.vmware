#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.vmware
Version  : 2.0.0
Release  : 21
URL      : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.0.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.vmware/oslo.vmware-2.0.0.tar.gz
Summary  : Oslo VMware library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.vmware-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : astroid-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : greenlet
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : iso8601
BuildRequires : linecache2-python
BuildRequires : logilab-common-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : netaddr-python
BuildRequires : netifaces
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pylint-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : retrying
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : suds-jurko
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : urllib3
BuildRequires : virtualenv

%description
===================================================
oslo.vmware --- VMware support code for OpenStack
===================================================

%package python
Summary: python components for the oslo.vmware package.
Group: Default
Requires: Babel-python
Requires: oslo.i18n-python
Requires: requests-python
Requires: six-python
Requires: stevedore

%description python
python components for the oslo.vmware package.


%prep
%setup -q -n oslo.vmware-2.0.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
