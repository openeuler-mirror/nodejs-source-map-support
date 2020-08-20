%{?nodejs_find_provides_and_requires}
%global packagename source-map-support
%global enable_tests 1
Name:                nodejs-source-map-support
Version:             0.4.18
Release:             1
Summary:             Fixes stack traces for files with source maps
License:             MIT
URL:                 https://github.com/evanw/node-source-map-support
Source0:             https://registry.npmjs.org/source-map-support/-/source-map-support-%{version}.tgz
Source1:             https://raw.githubusercontent.com/evanw/node-source-map-support/v%{version}/test.js
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(source-map)
%if 0%{?enable_tests}
BuildRequires:       mocha
%endif
%description
Fixes stack traces for files with source maps

%prep
%autosetup -n package
cp -p %{SOURCE1} .
%nodejs_fixdep source-map

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
        %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Aug 12 2020 zhanghua <zhanghua40@huawei.com> - 0.4.18-1
- package init
