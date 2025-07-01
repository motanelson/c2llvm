// Copyright 2011 The Emscripten Authors.  All rights reserved.
// Emscripten is available under two separate licenses, the MIT license and the
// University of Illinois/NCSA Open Source License.  Both these licenses can be
// found in the LICENSE file.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <time.h>
#include <math.h>

#include <emscripten.h>

void kernel_main(){
    time_t rawtime;
    struct tm * timeinfo;

    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    printf ( "%s\n", asctime (timeinfo) );
}

int main() {
    emscripten_set_main_loop(kernel_main,1,0);
    return 0;
}
