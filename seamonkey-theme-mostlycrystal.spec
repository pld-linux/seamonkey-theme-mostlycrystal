%define		_realname	mostlycrystal
Summary:	Mostly Crystal for SeaMonkey
Summary(pl):	Motyw Mostly Crystal do SeaMonkey
Name:		seamonkey-theme-mostlycrystal
Version:	2006.04.17
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://catthief.com/mozilla/downloads/%{_realname}_sea_1.jar
# Source0-md5:	a8e0a548a173f0ad3b7fc447ad32cb58
Source1:	gen-installed-chrome.sh
URL:		http://www.tom-cat.com/mozilla/seamonkey.html
Requires(post,postun):	seamonkey >= 1.0
Requires(post,postun):	textutils
Requires:	seamonkey >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
Mostly Crystal is a theme for the SeaMonkey "mostly" from the Crystal
SVG (for Linux) icon set designed by Everaldo and includes icons in
their original form plus custom-edited composites of the originals.

%description -l pl
Mostly Crystal jest motywem dla SeaMonkeya pochodz�cym g��wnie z
zestawu ikon Crystal SVG (for Linux) zaprojektowanego przez Everaldo i
zawiera ikony w ich oryginalnej formie oraz w�asnor�czne modyfikacje.

%prep
%setup -q -c -T
install %{SOURCE0} %{_realname}.jar
install %{SOURCE1} .
./gen-installed-chrome.sh skin %{_realname}.jar \
	> %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
