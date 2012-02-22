# Spec is based on Enrico Chiaretti's work in MIB and
# Erdem U. Altinyurt's and Toni Graffy's work in OpenSUSE(?)

%define oname DivFix++

Name:		divfix++
Summary:	A program to repair broken AVI file streams by rebuilding index part of file
Version:	0.34
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://divfixpp.sourceforge.net/
Source0:	%{oname}_v%{version}-src.tar.bz2
BuildRequires:	dos2unix
BuildRequires:	wxgtku-devel
%rename		%{oname}

%description
This program designed to repair broken AVI file streams by
rebuilding index part of file. This is very useful when trying
to preview movies which has no index part, like some files are
currently downloading from ed2k or bittorent networks.

DivFix++ has supports CLI tools, this means you can fix, preview
and delete movies automatically via script (by using argument
parameters...)

DivFix++ program code supports lots of operating system, because
it's writen by cross-platform API, wxWidgets.

%prep
%setup -q -n %{oname}_v%{version}
dos2unix docs/*
%__chmod 644 docs/*

%build
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# Overwite .desktop file
cat > %{buildroot}%{_datadir}/applications/%{oname}.desktop << EOF
[Desktop Entry]
Name=DivFix++
Comment=AVI Repair & Preview Utility
Exec=DivFix++
Icon=DivFix++
Terminal=false
Type=Application
Categories=AudioVideo;Video;
EOF

%find_lang %{oname}

%clean
%__rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc docs/*
%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{oname}.png

