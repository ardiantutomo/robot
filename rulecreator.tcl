#############################################################################
# Generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#  Jun 15, 2020 02:35:00 PM +07  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) -font {{Segoe UI} 11} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop44" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 700x580+507+189
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 124 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Patchio-Rule creator"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $top.scr48 \
        -background $vTcl(actual_gui_bg) -height 353 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 677 
    vTcl:DefineAlias "$top.scr48" "ActionTree" vTcl:WidgetProc "Toplevel1" 1

    .top43.scr48.01 configure -columns Col1 \
        -height 4
        .top43.scr48.01 configure -columns {Col1}
        .top43.scr48.01 heading #0 -text {Tree}
        .top43.scr48.01 heading #0 -anchor center
        .top43.scr48.01 column #0 -width 329
        .top43.scr48.01 column #0 -minwidth 20
        .top43.scr48.01 column #0 -stretch 1
        .top43.scr48.01 column #0 -anchor w
        .top43.scr48.01 heading Col1 -text {Col1}
        .top43.scr48.01 heading Col1 -anchor center
        .top43.scr48.01 column Col1 -width 329
        .top43.scr48.01 column Col1 -minwidth 20
        .top43.scr48.01 column Col1 -stretch 1
        .top43.scr48.01 column Col1 -anchor w
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Add 
    vTcl:DefineAlias "$top.but49" "btn_add_keyboard" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 264 
    vTcl:DefineAlias "$top.ent50" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Keyboard action} 
    vTcl:DefineAlias "$top.lab51" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Find image and right click} 
    vTcl:DefineAlias "$top.but52" "tn_add_image_right_click" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Find image and left click} 
    vTcl:DefineAlias "$top.but54" "btn_add_image_left_click" vTcl:WidgetProc "Toplevel1" 1
    button $top.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Save 
    vTcl:DefineAlias "$top.but55" "btn_save" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Delete Action} 
    vTcl:DefineAlias "$top.but44" "btn_delete" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Command 
    vTcl:DefineAlias "$top.lab44" "Label2" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex45 \
        -background white -font TkTextFont -foreground black -height 30 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 264 -wrap word 
    $top.tex45 configure -font "TkTextFont"
    $top.tex45 insert end text
    vTcl:DefineAlias "$top.tex45" "txt_command" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Add command} 
    vTcl:DefineAlias "$top.but46" "btn_add_command" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Wait action(ms)} 
    vTcl:DefineAlias "$top.lab47" "Label3" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex48 \
        -background white -font TkTextFont -foreground black -height 30 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 114 -wrap word 
    $top.tex48 configure -font "TkTextFont"
    $top.tex48 insert end text
    vTcl:DefineAlias "$top.tex48" "Text1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Add 
    vTcl:DefineAlias "$top.but50" "btn_add_wait_action" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Patchio V.1.0 By IO18-2} 
    vTcl:DefineAlias "$top.lab52" "Label4" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.scr48 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.022 -width 0 -relwidth 0.967 \
        -height 0 -relheight 0.588 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.429 -y 0 -rely 0.667 -width 47 -relwidth 0 \
        -height 41 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.667 -width 264 -relwidth 0 \
        -height 42 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx -0.014 -y 0 -rely 0.617 -width 0 -relwidth 0.213 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.529 -y 0 -rely 0.717 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.529 -y 0 -rely 0.65 -width 168 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.786 -y 0 -rely 0.65 -width 130 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 0 -relx 0.786 -y 0 -rely 0.717 -width 130 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.759 -width 0 -relwidth 0.1 \
        -height 0 -relheight 0.041 -anchor nw -bordermode ignore 
    place $top.tex45 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.793 -width 0 -relwidth 0.377 \
        -height 0 -relheight 0.05 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.429 -y 0 -rely 0.793 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.845 -width 0 -relwidth 0.14 \
        -height 0 -relheight 0.041 -anchor nw -bordermode ignore 
    place $top.tex48 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.879 -width 0 -relwidth 0.163 \
        -height 0 -relheight 0.05 -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.879 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.786 -y 0 -rely 0.966 -width 0 -relwidth 0.21 \
        -height 0 -relheight 0.041 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

