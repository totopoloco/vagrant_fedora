Name:           hello
Version:        0.0.1        
Release:        1%{?dist}
Summary:        A simple hello world program

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
A simple hello world program

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}.sh

%changelog
* Mon Jun  10 2024 Marco Tulio Ávila Cerón <marco.avila@nagarro.com> - 0.0.1
- First version being packaged