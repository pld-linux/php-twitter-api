%define		pkgname	twitter-api
%define		php_min_version 5.1.2
Summary:	Simple PHP Wrapper for Twitter API v1.1 calls
Name:		php-%{pkgname}
Version:	1.0.5
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/J7mbo/twitter-api-php/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2233db5ea90b598840f9f0f969893f77
URL:		https://github.com/J7mbo/twitter-api-php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(date)
Requires:	php(hash)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple PHP Wrapper for Twitter API v1.1 calls.

%prep
%setup -q -n twitter-api-php-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p TwitterAPIExchange.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%{php_data_dir}/TwitterAPIExchange.php
