import 'package:fcode_common/fcode_common.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'template_bloc.dart';
import 'template_state.dart';

class TemplateView extends StatelessWidget {
  static final log = Log("TemplateView");
  static final loadingWidget = Center(
    child: CircularProgressIndicator(),
  );

  @override
  Widget build(BuildContext context) {
    final templateBloc = BlocProvider.of<TemplateBloc>(context);
    final rootBloc = BlocProvider.of<RootPageBloc>(context);
    log.d("Loading Template View");

    CustomSnackBar customSnackBar;
    final scaffold = Scaffold(
      body: BlocBuilder<TemplateBloc, TemplateState>(
          condition: (pre, current) => true,
          builder: (context, state) {
            return Center(
              child: Text("HI..."),
            );
          }),
    );

    return MultiBlocListener(
      listeners: [
        BlocListener<TemplateBloc, TemplateState>(
          condition: (pre, current) => pre.error != current.error,
          listener: (context, state) {
            if (state.error?.isNotEmpty ?? false) {
              customSnackBar?.showErrorSnackBar(state.error);
            } else {
              customSnackBar?.hideAll();
            }
          },
        ),
      ],
      child: scaffold,
    );
  }
}
