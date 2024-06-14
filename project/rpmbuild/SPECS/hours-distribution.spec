Name:           hours-distribution
Version:        0.0.1        
Release:        1%{?dist}
Summary:        A Spring Boot application that exposes a REST API to distribute hours among employees.

License:        MIT
Source0:        %{name}.jar

Requires:       bash, java-21-openjdk
BuildArch:      noarch

%description
A Spring Boot application that exposes a REST API to distribute hours among employees.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{_sourcedir}/%{name}.jar $RPM_BUILD_ROOT/%{_bindir}

%post
echo "[Unit]
Description=Hours Distribution Service
After=syslog.target

[Service]
User=root
ExecStart=/usr/bin/java -jar /usr/bin/%{name}.jar
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/%{name}.service

systemctl daemon-reload
systemctl enable %{name}.service
systemctl start %{name}.service

%preun
systemctl stop %{name}.service
systemctl disable %{name}.service
rm /etc/systemd/system/%{name}.service
systemctl daemon-reload

%files
%{_bindir}/%{name}.jar

%changelog
* Mon Jun  10 2024 Marco Tulio Ávila Cerón <marco.avila@nagarro.com> - 0.0.1
- First version being packaged