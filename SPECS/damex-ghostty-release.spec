%define debug_package %{nil}
%define disttype %{expand:%%(/usr/lib/rpm/redhat/dist.sh --disttype)}
%define distnum %{expand:%%(/usr/lib/rpm/redhat/dist.sh --distnum)}
%undefine source_date_epoch_from_changelog

Name: damex-ghostty-release
Version: 0.1.0
Release: 1%{?dist}
Summary: damex ghostty repository configuration
License: MIT
URL: https://yum-repositories.damex.org

%description

%prep

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/yum.repos.d
cat <<EOF > %{buildroot}%{_sysconfdir}/yum.repos.d/damex-ghostty.repo
[damex-ghostty]
name = damex-ghostty
baseurl = https://yum-repositories.damex.org/ghostty/%{disttype}/%{distnum}/%{_arch}
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/ghostty/ghostty-2036-09-27.asc
EOF

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/damex-ghostty.repo
