%define debug_package %{nil}

Name: damex-ghostty-release
Version: 0.1.0
Release: 2%{?dist}
Summary: damex ghostty repository configuration
License: MIT
URL: https://yum-repositories.damex.org
BuildArch: noarch

%description
This package contains the damex-ghostty repository configuration.

%prep

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/yum.repos.d
%{__cat} <<'EOF' > %{buildroot}%{_sysconfdir}/yum.repos.d/damex-ghostty.repo
[damex-ghostty]
name = damex-ghostty
baseurl = https://yum-repositories.damex.org/ghostty/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/ghostty/ghostty-2036-09-27.asc
EOF

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/damex-ghostty.repo

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/ghostty/commits/production
