#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-xattr
Version  : 1.4.0
Release  : 42
URL      : https://pecl.php.net/get/xattr-1.4.0.tgz
Source0  : https://pecl.php.net/get/xattr-1.4.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-xattr-lib = %{version}-%{release}
Requires: php-xattr-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-xattr package.
Group: Libraries
Requires: php-xattr-license = %{version}-%{release}

%description lib
lib components for the php-xattr package.


%package license
Summary: license components for the php-xattr package.
Group: Default

%description license
license components for the php-xattr package.


%prep
%setup -q -n xattr-1.4.0
cd %{_builddir}/xattr-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-xattr
cp %{_builddir}/xattr-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-xattr/23cb6fa873d559515b754db54720962118c95899
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/xattr.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-xattr/23cb6fa873d559515b754db54720962118c95899
