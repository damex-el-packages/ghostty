%undefine source_date_epoch_from_changelog

Name: gtk4-layer-shell
Version: 1.3.0
Release: 1%{?dist}
Summary: Library to create panels and other desktop components for Wayland
License: MIT
URL: https://github.com/wmww/gtk4-layer-shell
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(wayland-client) >= 1.10.0
BuildRequires: pkgconfig(wayland-protocols) >= 1.16
BuildRequires: pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires: pkgconfig(wayland-server) >= 1.10.0

%package -n %{name}-devel
Summary: Development files for gtk4-layer-shell
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
Library for using the Layer Shell and Session Lock Wayland protocols with GTK4.

%description -n %{name}-devel
Development files for gtk4-layer-shell.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/girepository-1.0/Gtk4LayerShell-1.0.typelib
%{_libdir}/girepository-1.0/Gtk4SessionLock-1.0.typelib
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.0

%files -n %{name}-devel
%{_datadir}/gir-1.0/Gtk4LayerShell-1.0.gir
%{_datadir}/gir-1.0/Gtk4SessionLock-1.0.gir
%{_datadir}/vala/vapi/gtk4-layer-shell-0.deps
%{_datadir}/vala/vapi/gtk4-layer-shell-0.vapi
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/liblayer-shell-preload.so
%{_libdir}/pkgconfig/gtk4-layer-shell-0.pc
