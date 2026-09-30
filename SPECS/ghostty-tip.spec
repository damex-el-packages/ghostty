%define debug_package %{nil}
%undefine source_date_epoch_from_changelog
%global build_date %(date -u +%%Y%%m%%d)

Name: ghostty-tip
Version: %{build_date}
Release: 1%{?dist}
Summary: Fast, feature-rich and cross-platform terminal emulator built from upstream tip
License: MIT
URL: https://ghostty.org
Source0: https://github.com/ghostty-org/ghostty/releases/download/tip/ghostty-source.tar.gz
BuildRequires: blueprint-compiler
BuildRequires: gettext
BuildRequires: pandoc
BuildRequires: zig
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(x11)
Provides: ghostty = %{version}-%{release}
Conflicts: ghostty

%description
Ghostty terminal emulator built from upstream tip.

%prep
%setup -q -c -T
%{__tar} --extract --file %{SOURCE0} --strip-components=1

%build

%install
DESTDIR=%{buildroot} zig build --prefix %{_prefix} --global-cache-dir %{_builddir}/zig-global-cache -Doptimize=ReleaseFast -Dcpu=baseline -Dpie=true
%{__rm} -r %{buildroot}%{_includedir}/ghostty
%{__rm} %{buildroot}%{_prefix}/lib/libghostty-vt.a %{buildroot}%{_prefix}/lib/libghostty-vt.so %{buildroot}%{_prefix}/lib/libghostty-vt.so.0 %{buildroot}%{_prefix}/lib/libghostty-vt.so.0.1.0
%{__rm} %{buildroot}%{_datadir}/pkgconfig/libghostty-vt.pc %{buildroot}%{_datadir}/pkgconfig/libghostty-vt-static.pc
%find_lang com.mitchellh.ghostty

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
%dir %{_datadir}/systemd/user
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
%{_datadir}/systemd/user/app-com.mitchellh.ghostty.service
%{_datadir}/terminfo/g/ghostty
%{_datadir}/terminfo/x/xterm-ghostty
%{_datadir}/vim/vimfiles/compiler/ghostty.vim
%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
%{_datadir}/vim/vimfiles/syntax/ghostty.vim
%{_datadir}/zsh/site-functions/_ghostty
%{_mandir}/man1/ghostty.1.gz
%{_mandir}/man5/ghostty.5.gz
