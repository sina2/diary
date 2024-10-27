#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "<HTML>\n<HEAD>\n";
print "<meta name=robots content=noindex>\n";
print "<title></title>\n";
print "</head>\n";
print "<BODY TEXT=\"#80ffff\" LINK=\"#ffff80\" VLINK=\"#80ff00\" ALINK=\"#ff0080\" BGCOLOR=\"#0080ff\">\n";

printf "<font size=+2></font>\n";


open( IN ,"/bin/ls -rF |/bin/grep -E \"[0-9]+/\" |");
while (<IN>) {

  $temp = $_ ;
  $temp =~ s/([0-9][0-9][0-9][0-9])([0-9][0-9])\/\n/$1$2/g ;
  $year = $1 ;
  $month = $2 ;
  $month =~ s/([0])([0-9])/$2/g ;

  if( $pre_year ne $year ){
    printf "<BR><BR><table bgcolor=\"#3717a4\" width=100%><tr><td><font size=+2 color=white>Year ". $year ."</font></td></tr></table>\n";
    $pre_year = $year;
  }
    print "<div align=center><a href=" . $temp . "/ target=diary>Month " . $month . "</a><BR></div>\n";
};
close(IN);


print "<BR><BR><HR>\n";
print "</body></html>\n";



















