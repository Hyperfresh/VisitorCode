# Paul Asencion (Hy~) 11JHAR
# Planning and programming a visitor register
# Concordia College | SACE 740975X

# Code will eventually appear™
logo = """
             '    ix    `                                                                                                                                                                           
        `    ]V _`D9 _ ^z    `                                                                                                                                                                      
        <h~`ix@VEK@@IBu#yL!_yx                                                                                                                                                                      
       ,=v#9Q#@@@@@@@@@@#@O#y!=                                                                                                                                                                     
   _xyLx$#@@@@@@@dkkZ#@@@@@@#Blvu\-                                                                                                                                                                 
    `*zEQQBQ$MKeI6QQ6jkjmdgQQQ0s\                                                                                                                                                                   
    )@Q0bGHM6$gdy~``~}W$$EMHHME$#r               >TmZOdMjx"      `*c3dOdGy(_     -oooz=     -zooo<     _\wWdOZau^`      :xoMOOZs}~`    `uooooooojy};`    |oooooojy})-      roooy.      `cPPPK:      
   _Qg__:=~!"'  `....`  `_!~~!,`zQ_            v$@@@@@@@@@@R^  .cB@@@@@@@@@@O^   !@@@@@z'   =@@@@V   ^6@@@@@@@@@@#w  `i8@@@@@@@@@@B|   .B@@@@@@@@@@@#u`  M@@@@@@@@@@@0i`   3@@@#,      k@@@@@g-     
  _0B:    .*?>` !UUUU)   !)r-   `B$_         `M@@@@RVxYsB@BX! !Q@@@#G}x}K#@@@@k` !@@@@@@Q*  =@@@@V  w@@@@BeYxV6@@Rx _0@@@@$yxxVD@@@@M' .B@@@Q}}}uM@@@@c  M@@@#oVym$@@@@g"  3@@@#,     i@@@@@@@d`    
 *B$"    >#3x}- !hhUU) `bgxT;    ,0B*        V@@@#r     `<`  `g@@@D-     .b@@@@x !@@@@@@@@3-=@@@@V v@@@@d.     ::   M@@@@x      r#@@@w .B@@@Z     O@@@G  M@@@B-    =@@@@O  3@@@#,    *#@@@s#@@@h    
M@c      >B3]y, !UUhh) `Z8]y)      y@5`      9@@@M           ;@@@@)       ~@@@@G !@@@@oQ@@@#d@@@@V K@@@@^          _#@@@R        G@@@$ .B@@@#MMMdB@@@Q!  M@@@#-     6@@@#_ 3@@@#,   ^#@@@} ~#@@@I   
-9#=      -rv^` !hhUh(` `~v)_     ^#d-       X@@@#=      :`  -B@@@d'     `s@@@@} !@@@@~.I@@@@@@@@V L@@@@a`     .,  `R@@@#r      !B@@@U .B@@@@@@@@@@gx'   M@@@#-    _#@@@R` 3@@@#,  `B@@@#qPPB@@@@}  
 .Q8'  )yyyyyyyykUUhhoyywyyywyT` -B$`        -$@@@#av*rTD@BU~ *#@@@Qyr<rug@@@@G` !@@@@~  ~g@@@@@@V `M@@@@8ur*ve#@Ei`!B@@@@Z]^^va#@@@D- .B@@@D:=M@@@#r    M@@@#}vxu5#@@@Q:  3@@@#,  X@@@@@@@@@@@@@@r 
  Y@|  vhUhUUUUUhUhhUhUhhhUhUhV` Y@v          'y#@@@@@@@@@@8r  :G#@@@@@@@@@@8v   !@@@@~   `c#@@@@V  `iQ@@@@@@@@@@#s` -X#@@@@@@@@@@#}`  .B@@@Z   }#@@@h`  M@@@@@@@@@@@QV.   3@@@#, Y@@@#)!!!!!;$@@@#!
  *@T  ~vvvvvvvv}UUUhVvvvvvvvvr` o@=            `xmR8QQ0Mc~      -}PE8QQ0GT=     _dddd"     :Pdddr    `^VZ$QQ86Uv-     'rkdgQQgdo?-    `mdddT    ~MdddT` }ddddddZWX}!      xdddG-_Hddb*       :MdddV
  \@]      _Y*^>]5KKMy<^*i:      c@*                                                                                                                                                                
  I@=     )YU^}TTLMj}TT}*Vvv     *@c                                                                                                                                                                
 .QE      wyI~i}T)yviT}i<ciX     `8g`            !vVjoy}*.      `=YyXzcv:      `v?           ^L.          !}}}}}}}}}}x`     _rTkIkur-    `v}}}}}}}}}}=                                              
 x@i      wyI!|xxrVxxxx\=c]X      c@r          (D8oxr*vV9#M_  -kB$u?*rimQQ}`   .BQ           Z@!          V@Miiiiiiiiv`   rEBGYr*)LZBU`  -B#}iiiiiiii!                                              
 EQ'      wyI:^**!V|<**^!ciX      _#Z        _g#(        `-  v#O_        >Q#~  .BQ           Z@!          V@v           -D#x             .B8`                                                       
!@U       wyI:**^!V|;^**!c]X       W#,       K@v            "#8'          =#$` .BQ           Z@!          V@]````````   z@Y              .BQ'```````                                                
}@)       wcqLL***Zz**^iY3vo       x@v       $#:            )@a           `8#, .BQ           Z@!          V@QEEEEEERG'  6@=     Y99RR0z  .B#DEEEEEEE(                                               
h@!       |}}#Bv}ozzIy|Q@Vv}       ^@y       K@x            :#Q.          =#0` .BQ           Z@!          V@v           X@L     `...!#R  .B8`                                                       
y@^         -dG`!sMGh) XE:         r@l       _g#v        `:  v#R"        ~QB!  .BQ           Z@!          V@v           -g#?        -#R  .B8`                                                       
:BD_            :yyyy*            ,$B,        'VBdL<::=veBR:  =d#M|=:!^}R#I-   .BB********!  Z@}*******<` V@h^^^^^^^^^`  'yB$u^:,:<uDBT  .BBr^^^^^^^^:                                              
 "aQ9zir~:::==!,'    `_!==!::!*xVRQm,           `?wWdd5ox:      _vUMdZ3c*'     `uhhhhhhhhhx  vhhhhhhhhhy' ^hhhhhhhhhhI_    `^uKZdZa}>`   `Vhhhhhhhhhh)                                              
   `:)ToGddZqWM9g9VV98DZWWMddMeVv:`                                                                                                                                                                 
                 ~zz=`                                                                                                                                                                              
"""
print(logo)