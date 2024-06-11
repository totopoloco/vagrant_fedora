Name:           hours-distribution
Version:        0.0.1        
Release:        1%{?dist}
Summary:        A Spring Boot application that exposes a REST API to distribute hours among employees.

License:        MIT
Source0:        %{name}.jar

Requires:       bash, java-21-openjdk

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
ExecStart=/usr/bin/java -jar /usr/bin/hours-distribution.jar
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/%{name}.service

systemctl daemon-reload
systemctl enable hours-distribution.service
systemctl start hours-distribution.service

%preun
systemctl stop hours-distribution.service
systemctl disable hours-distribution.service
rm /etc/systemd/system/hours-distribution.service
systemctl daemon-reload

%files
%{_bindir}/%{name}.jar

%changelog
* Mon Jun  10 2024 Marco Tulio Ávila Cerón <marco.avila@nagarro.com> - 0.0.1
- First version being packaged