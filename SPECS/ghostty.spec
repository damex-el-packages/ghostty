%global minisign_public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%global _zig_release_mode fast
%global _zig_system_integration --system "${PWD}/zig-pkg"

Name: ghostty
Version: 1.4.0
Release: 1%{?dist}
Summary: Fast, feature-rich and cross-platform terminal emulator
License: MIT
URL: https://ghostty.org
Source0: https://release.files.ghostty.org/%{version}/%{name}-%{version}.tar.gz
Source1: https://release.files.ghostty.org/%{version}/%{name}-%{version}.tar.gz.minisig
ExclusiveArch: x86_64
BuildRequires: blueprint-compiler
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: minisign
BuildRequires: pandoc
BuildRequires: zig >= 0.16.0
BuildRequires: zig-rpm-macros
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(oniguruma)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)

%description
Ghostty is a terminal emulator that differentiates itself by being fast,
feature-rich, and native. While there are many excellent terminal
emulators available, they all force you to choose between speed,
features, or native UIs. Ghostty provides all three.

%prep
minisign -V -P %{minisign_public_key} -m %{SOURCE0} -x %{SOURCE1}
%autosetup
%zig_prep
%{__zig} build --fetch=all %{_zig_fetch_options}

%build

%install
%zig_install -fno-sys=harfbuzz -Dstrip=false -Dversion-string=%{version}
%{__rm} -r %{buildroot}%{_includedir}/ghostty
%{__rm} %{buildroot}%{_libdir}/libghostty-vt.a %{buildroot}%{_libdir}/libghostty-vt.so %{buildroot}%{_libdir}/libghostty-vt.so.0 %{buildroot}%{_libdir}/libghostty-vt.so.0.1.0
%{__rm} %{buildroot}%{_datadir}/pkgconfig/libghostty-vt.pc %{buildroot}%{_datadir}/pkgconfig/libghostty-vt-static.pc
%fdupes %{buildroot}%{_datadir}
%find_lang com.mitchellh.ghostty

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.mitchellh.ghostty.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.mitchellh.ghostty.metainfo.xml

%files -f com.mitchellh.ghostty.lang
%license LICENSE
%dir %{_datadir}/bat
%dir %{_datadir}/bat/syntaxes
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions
%dir %{_datadir}/nvim
%dir %{_datadir}/nvim/site
%dir %{_datadir}/nvim/site/compiler
%dir %{_datadir}/nvim/site/ftdetect
%dir %{_datadir}/nvim/site/ftplugin
%dir %{_datadir}/nvim/site/syntax
%dir %{_datadir}/vim/vimfiles/compiler
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/ftplugin
%dir %{_datadir}/vim/vimfiles/syntax
%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{_datadir}/bash-completion/completions/ghostty.bash
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{_datadir}/dbus-1/services/com.mitchellh.ghostty.service
%{_datadir}/fish/vendor_completions.d/ghostty.fish
%{_datadir}/ghostty
%{_datadir}/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/1024x1024/apps/com.mitchellh.ghostty.png
%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_datadir}/metainfo/com.mitchellh.ghostty.metainfo.xml
%{_datadir}/nautilus-python/extensions/ghostty.py
%{_datadir}/nvim/site/compiler/ghostty.vim
%{_datadir}/nvim/site/ftdetect/ghostty.vim
%{_datadir}/nvim/site/ftplugin/ghostty.vim
%{_datadir}/nvim/site/syntax/ghostty.vim
%{_userunitdir}/app-com.mitchellh.ghostty.service
%{_datadir}/terminfo/g/ghostty
%{_datadir}/terminfo/x/xterm-ghostty
%{_datadir}/vim/vimfiles/compiler/ghostty.vim
%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
%{_datadir}/vim/vimfiles/syntax/ghostty.vim
%{_datadir}/zsh/site-functions/_ghostty
%{_mandir}/man1/ghostty.1.gz
%{_mandir}/man5/ghostty.5.gz

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/ghostty/commits/production
